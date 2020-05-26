
class UserTypes:
    """User can either be admin, writer or publisher"""
    ADMIN = "admin"
    WRITER = "writes"
    EDITOR = "editor"

    CUSTOM_TYPES = (
        (ADMIN, "Admin User"),
        (WRITER, "Writer"),
        (EDITOR, "Editor")
    )
