import React, { useEffect } from "react"
import { useDispatch, useSelector } from "react-redux"
import Post from "../../features/posts/Posts"
import { loadAllPosts, postSelectors } from "../../features/posts/postslice"
import { getState } from '../../store'


export default function MessageBoard() {
    const dispatch = useDispatch()

    useEffect(() => {
        dispatch(loadAllPosts())
    }, [dispatch])

    const posts = Object.values(useSelector((state)=>state.posts.entities))
    console.log(posts)

    return (
        <div className="container bg-transparent">
            <ul className="container-fluid bg-info">
                <div className="accordion" id="postAccordion">
                    { posts.map((post, index) => (
                        <li key={post.id}>
                            <Post post={post} index={index}/>
                        </li>
                    ))}
                </div>
            </ul>
        </div>
    )
}
