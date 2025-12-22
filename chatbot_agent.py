import requests

# Wikipedia helper (only for allowed subjects)
def get_summary(topic):
    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{topic}"
    try:
        res = requests.get(url, timeout=3)
        if res.status_code == 200:
            return res.json().get("extract", "I found information, but cannot explain clearly.")
        else:
            return "I could not find information on that topic."
    except:
        return "Internet issue. Please try again."

def chatbot_reply(message):
    msg = message.lower()

    # ---------- SQL ----------
    if "sql tool" in msg or "sql tools" in msg:
        return (
            "Common SQL tools:\n"
            "1. MySQL Workbench\n"
            "2. Oracle SQL Developer\n"
            "3. SQL Server Management Studio\n"
            "4. phpMyAdmin"
        )

    elif "sql command" in msg:
        return (
            "Basic SQL commands:\n"
            "SELECT, INSERT, UPDATE, DELETE"
        )

    elif "join" in msg:
        return "SQL JOIN is used to combine rows from multiple tables."

    elif "sql" in msg:
        return "SQL is used to store, retrieve, and manage data in databases."

    # ---------- OPERATING SYSTEM ----------
    elif "operating system" in msg or "os" in msg:
        return (
            "An Operating System acts as an interface between user and hardware. "
            "Examples: Windows, Linux, macOS."
        )

    elif "process" in msg:
        return "A process is a program in execution."

    elif "cpu scheduling" in msg:
        return "CPU scheduling decides which process gets CPU time."

    # ---------- NETWORK SECURITY ----------
    elif "network security" in msg:
        return (
            "Network security protects networks from unauthorized access and attacks."
        )

    elif "firewall" in msg:
        return "A firewall monitors and controls incoming and outgoing network traffic."

    elif "encryption" in msg:
        return "Encryption converts data into a secure format to prevent unauthorized access."

    # ---------- FALLBACK (ONLY THESE SUBJECTS) ----------
    elif any(word in msg for word in ["sql", "database", "query",
                                      "operating", "os", "process",
                                      "network", "security", "firewall"]):
        # Try Wikipedia for allowed domains
        return get_summary(msg.replace(" ", "_"))

    else:
        return (
            "⚠️ I support only the following subjects:\n"
            "• SQL\n"
            "• Operating System\n"
            "• Network Security\n\n"
            "Please ask questions from these topics only."
        )
