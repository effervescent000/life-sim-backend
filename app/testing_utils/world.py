from ..schema import User
from ..auth.models import UserWrite


def world_base_state():
    out = []
    out.append(
        User(
            **UserWrite(
                email="test@email.com",
                name="some person",
                hashed_password="a really strong password",
            ).dict()
        )
    )
    return out
