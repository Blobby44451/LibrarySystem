from database import get_connection

def add_member(name, email, phone):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO members (name, email, phone) VALUES (?, ?, ?)", (name, email, phone))
    conn.commit()
    conn.close()
    print(f"Member '{name}' added.")

def list_members():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM members")
    members = cursor.fetchall()
    conn.close()
    if not members:
        print("No members found.")
        return
    print("\n--- Members ---")
    for m in members:
        print(f"[{m[0]}] {m[1]} | {m[2]} | {m[3]}")

def update_member(member_id, name, email, phone):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE members SET name=?, email=?, phone=? WHERE id=?", (name, email, phone, member_id))
    conn.commit()
    conn.close()
    print(f"Member ID {member_id} updated.")

def delete_member(member_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM members WHERE id=?", (member_id,))
    conn.commit()
    conn.close()
    print(f"Member ID {member_id} deleted.")