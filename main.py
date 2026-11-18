from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI(
    title="fastapi-pydantic",
    description="practice fastapi+pydantic restful",
)



@app.get("/")
async def health():
    return {"message": "health 200"}



@app.post("/api/posts", status_code=status.HTTP_201_CREATED)
async def create_post(body: PostCreate) -> Post:
    if any(post.caption == body.caption for post in post_example):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="postingan duplikat",
        )
    
    new_post = Post(**body.model_dump())
    post_example.append(new_post)
    return new_post


@app.patch("/api/posts/{caption}")
def update_post(caption: str, body: PostUpdate) -> Post:
    for post in post_example:
        if post.caption == caption:
            if body.caption is not None:
                post.caption = body.caption
            if body.content is not None:
                post.content = body.content
            return post

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="post tidak ditemukan",
    )


@app.delete("/api/posts/{caption}", status_code=status.HTTP_200_OK)
async def delete_post(caption: str) -> dict:
    before = len(post_example)
    post_example[:] = [post for post in post_example if post.caption != caption]

    if len(post_example) == before:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="post tidak ditemukan",
        )

    return {
        "message": "berhasil menghapus",
        "total": len(post_example),
        "data": post_example,
    }
