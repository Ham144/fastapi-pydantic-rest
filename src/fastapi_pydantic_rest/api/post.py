

from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, Field
from starlette.status import HTTP_404_NOT_FOUND


router = APIRouter(
    prefix="/api/posts",
    tags=["Post"]
)

class PostCreate(BaseModel):
    caption: str
    content: str
    tags: list[str] = Field(default_factory=list)


class PostUpdate(BaseModel):
    caption: str | None = None
    content: str | None = None


class Post(BaseModel):
    caption: str
    content: str
    tags: list[str]


post_example: list[Post] = [
    Post(
        caption="hey morning",
        content="today i feel happy",
        tags=["morning", "day", "good day"],
    ),
    Post(
        caption="this is my first day to get to work",
        content="i am happy now i have a job",
        tags=["happy", "gratefull", "ponder"],
    ),
]

@router.post("/", status_code=status.HTTP_201_CREATED)
async def publish_product(body: Post):
    before = len(post_example)
    for post in post_example:
        if post["caption"] == body.caption:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="post duplicate"
            )
    
    post_example.append(**body.model_dump())
    if len(post_example) == before:
        raise HTTPException(
            status_code=HTTP_404_NOT_FOUND
        )
    
    return {
        "status_code": 200,
        "data": post_example,
        "total": len(post_example)
    }
            

@router.patch("/{caption_to_edit}")
async def update_post()