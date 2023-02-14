from ..schema import User
from ..auth.models import UserWrite


def world_base_state():
    out = []
    out.append(
        User(
            **UserWrite(
                email="test@email.com",
                username="some person",
                hashed_password="a really strong password",
            ).dict()
        )
    )
    return out
