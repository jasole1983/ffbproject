import React, { useEffect } from "react"
import { useDispatch, useSelector } from "react-redux"
import Post from "../../features/posts/Posts"
import { loadAllPosts, postSelectors } from "../../features/posts/postslice"
import { loadAllComments } from "../../features/comments/commentSlice"
import Comment from "../../features/comments/Comments"



export default function MessageBoard() {
    const dispatch = useDispatch()

    useEffect(() => {
        dispatch(loadAllPosts())
        dispatch(loadAllComments())
    }, [dispatch])

    const posts = Object.values(useSelector((state)=>state.posts.entities))
 
    console.log(posts)

    return (
        <>
            <div className="container-fluid bg-info">    
                        { posts.map((post, index) => (    
                            <Post post={post} index={index} key={post.id} />
                            ))}
            </div>
        </>
    )
}
