import React from 'react'
import Comment from '../comments/Comments'
import { Button } from 'react-bootstrap'


export default function Post({ post, index }) {
    const title = post.title
    const body = post.body
    const franchise = post.franchise
    const convertedDate = post.created.slice(0,10)
    console.log({'created': post.created})
    const cd = new Date(convertedDate)
    const created = cd.toUTCString()
    const comments = post.comments
    const collapsed = [`post${index}body`, `post${index}comments`]


    return (
        <div className="card bg-dark text-light">

            <div className="card-header " id={`post${index}header`}>
                <h6 className="mb-0 d-flex justify-content-between">
                    <button className="btn btn-link text-decoration-none" type="button" data-toggle="collapse" data-target=".multi-collapse" aria-expanded="false" aria-controls={collapsed.join(' ')}>{title}</button>
                    <span>{franchise}</span><span>{created}</span>
                </h6>
            </div>
            <div className="collapse multi-collapse" id={`post${index}body`}>
                <div className="card-body border border-color-warning">
                    <p className="card-text">{body}</p>
                </div>
            </div>
            <div className="collapse multi-collapse" id={`post${index}comments`}>
                {comments.map((comment, idx) => (
                    <Comment comment={comment} idx={idx} index={index} key={comment.id} />
                    ))}
                
                <form className="form-group">
                <div className="input-group">
                    <input type="text" className="form-control" aria-label="Comment on this Post"/>
                    <div className="input-group-append">
                        <button className="btn btn-primary rounded" type="button">REPLY</button>
                    </div>
                </div>
                <div className="container bg-transparent mb-3">
                    <input type="hidden" id="TBD"/>
                    <input type="hidden" id="TBD"/>
                    <input type="hidden" id="TBD"/>
                </div>
                </form>
            </div>
        </div>
             
        
    )
}