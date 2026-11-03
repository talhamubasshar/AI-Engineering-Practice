"""
Day 1: Python Data Structures, Type Hints & Comprehensions for TypeScript Devs.
"""
from typing import Any


# 1. Custom Exception Class (Similar to extending Error in TS)
class UserValidationError(Exception):
    """Raised when a user record has invalid or missing data."""
    pass


# 2. Typed Function (Notice type annotations: list[dict], str, float, etc.)
def process_user_records(raw_users: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """
    Sanitizes raw user dictionaries, filters active users,
    and applies a tier calculation.
    """
    processed: list[dict[str, Any]] = []

    for user in raw_users:
        try:
            # Check required keys
            if "email" not in user or "name" not in user:
                raise UserValidationError(f"Record {user.get('id', 'unknown')} missing email or name")
                
            # Extract and sanitize
            user_id: int = user["id"]
            name: str = user["name"].strip().title()
            email: str = user["email"].strip().lower()
            is_active: bool = user.get("is_active", False)
            spend: float = float(user.get("total_spend", 0.0))

            # Only process active users
            if not is_active:
                continue

            # Python ternary operator: VALUE_IF_TRUE if CONDITION else VALUE_IF_FALSE
            tier: str = "VIP" if spend >= 100.0 else "Standard"

            processed.append({
                "id": user_id,
                "name": name,
                "email": email,
                "tier": tier,
                "spend": spend,
            })

        except (ValueError, UserValidationError) as err:
            print(f"[WARNING] Skipping corrupt record: {err}")
            continue

    return processed


def main() -> None:
    # Raw mock payload (like what you'd receive from an API or database)
    raw_payload: list[dict[str, Any]] = [
        {"id": 1, "name": "   talha mubashar ", "email": "Talha@Example.COM", "is_active": True, "total_spend": 149.50},
        {"id": 2, "name": "Ayesha Khan", "email": "ayesha@company.pk", "is_active": False, "total_spend": 25.00},
        {"id": 3, "name": "corrupt record", "is_active": True},  # Missing email
        {"id": 4, "name": "hamza ali", "email": "hamza@domain.com", "is_active": True, "total_spend": 89.00},
        {"id": 5, "name": "hammad", "email": "hammad@domain.com", "is_active": True, "total_spend": 210.00}
    ]

    print("--- Processing Raw Users ---")
    active_users = process_user_records(raw_payload)

    print("\n--- Processed Active Users ---")
    for u in active_users:
        print(f"User #{u['id']}: {u['name']} <{u['email']}> | Tier: {u['tier']} | Spend: ${u['spend']:.2f}")

    # 3. List Comprehension (.map / .filter)
    # Get all VIP user emails in one clean line:
    vip_emails: list[str] = [u["email"] for u in active_users if u["tier"] == "VIP"]
    print(f"\nVIP Emails (via list comprehension): {vip_emails}")

    # 4. Dict Comprehension (Transforming array into a lookup map by ID)
    # Equivalent to reduce in JS: users.reduce((acc, u) => ({ ...acc, [u.id]: u.name }), {})
    user_lookup_by_id: dict[int, str] = {u["id"]: u["name"] for u in active_users}
    print(f"User Lookup Map (via dict comprehension): {user_lookup_by_id}")


if __name__ == "__main__":
    main()

