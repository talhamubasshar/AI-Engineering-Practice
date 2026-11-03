"""
Day 2: Async Python & Modern Typing with httpx and asyncio.
Comparing Sequential Execution vs. Concurrent Execution (Promise.all equivalent).
"""
import asyncio
import time
from typing import Any
import httpx


# The endpoints we want to fetch (5 different post IDs)
ENDPOINT_IDS: list[int] = [1, 2, 3, 4, 5]
BASE_URL: str = "https://jsonplaceholder.typicode.com/posts"


# =====================================================================
# 1. THE SLOW WAY: Synchronous / Sequential Execution
# =====================================================================
def fetch_post_sync(post_id: int) -> dict[str, Any]:
    """
    Fetches a single post synchronously.
    Blocks the entire Python thread while waiting for the network response.
    """
    url: str = f"{BASE_URL}/{post_id}"
    try:
        response = httpx.get(url, timeout=5.0)
        response.raise_for_status()
        data = response.json()
        return {"id": data["id"], "title": data["title"]}
    except httpx.HTTPError as err:
        return {"id": post_id, "error": str(err)}


def run_sequential_benchmark() -> float:
    """Runs all 5 requests one after another."""
    print("\n--- Running Sequential (One-by-One) ---")
    start_time = time.perf_counter()

    results: list[dict[str, Any]] = []
    for p_id in ENDPOINT_IDS:
        print(f"Fetching Post #{p_id} sequentially...")
        post = fetch_post_sync(p_id)
        results.append(post)

    elapsed = time.perf_counter() - start_time
    print(f"Sequential Finished! Fetched {len(results)} items in {elapsed:.2f}s")
    return elapsed


# =====================================================================
# 2. THE FAST WAY: Asynchronous / Concurrent Execution
# =====================================================================
async def fetch_post_async(client: httpx.AsyncClient, post_id: int) -> dict[str, Any]:
    """
    Fetches a single post asynchronously.
    Yields control back to the event loop while waiting for the network socket!
    (Equivalent to `const res = await fetch(...)` in JS).
    """
    url: str = f"{BASE_URL}/{post_id}"
    try:
        response = await client.get(url, timeout=5.0)
        response.raise_for_status()
        data = response.json()
        return {"id": data["id"], "title": data["title"]}
    except httpx.HTTPError as err:
        print(f"[ERROR] Failed fetching post #{post_id}: {err}")
        return {"id": post_id, "error": str(err)}


async def run_async_benchmark() -> float:
    """
    Fires all 5 requests concurrently using asyncio.gather.
    (Equivalent to `await Promise.all(...)` in JavaScript).
    """
    print("\n--- Running Asynchronous (All at once via asyncio.gather) ---")
    start_time = time.perf_counter()

    # `async with` creates a shared HTTP connection pool and auto-closes it
    async with httpx.AsyncClient() as client:
        # Create a list of 5 pending coroutines (like an array of pending Promises in JS)
        tasks = [fetch_post_async(client, p_id) for p_id in ENDPOINT_IDS]

        # `asyncio.gather(*tasks)` fires all of them concurrently!
        # The `*` unpacks the list of tasks (spread operator in JS: Promise.all([...tasks]))
        results: list[dict[str, Any]] = await asyncio.gather(*tasks)

    elapsed = time.perf_counter() - start_time
    print(f"Async Finished! Fetched {len(results)} items in {elapsed:.2f}s")

    print("\nSample Fetched Posts:")
    for r in results[:2]:
        print(f"• #{r['id']}: \"{r.get('title', '')[:40]}...\"")

    return elapsed


# =====================================================================
# 3. MAIN RUNNER & BENCHMARK COMPARISON
# =====================================================================
def main() -> None:
    print("=" * 60)
    print("DAY 2 BENCHMARK: Synchronous vs. Asynchronous HTTP in Python")
    print("=" * 60)

    # 1. Run sequential
    seq_time = run_sequential_benchmark()

    # 2. Run async (asyncio.run starts the Python event loop)
    async_time = asyncio.run(run_async_benchmark())

    # 3. Compare speedup
    speedup = seq_time / async_time if async_time > 0 else 1.0
    print("\n" + "=" * 60)
    print("BENCHMARK RESULTS:")
    print(f"• Sequential Time : {seq_time:.2f} seconds")
    print(f"• Async Time      : {async_time:.2f} seconds")
    print(f"• Speedup Factor  : {speedup:.1f}x faster with asyncio!")
    print("=" * 60)


if __name__ == "__main__":
    main()
