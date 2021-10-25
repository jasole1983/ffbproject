import React from 'react'


export default function Post({ post, index }) {
    const title = post.title
    const body = post.body
    const franchise = post.franchise
    const create = post.create_date


    return (
        
        <div className="card text-white border-info bg-dark mb-3 w-50 rounded-lg">
            <div className="card-header" id={`heading-${index}`}>
                <button className="btn btn-link" type="button" data-toggle="collapse" data-target={`#postbody-${index}`} aria-expanded="true" aria-controls={`postbody-${index}`}>    
                    <h5 className="card-title justify-contents-start">{title}</h5>
                </button>
                <h6 className="justify-contents-center">{franchise}</h6>
                <h6 className="justify-contents-end">{create}</h6>
            </div>
            <div id={`postbody-${index}`} className="collapse show" aria-labelledby={`heading-${index}`} data-parent="postAccordion">
                <div className="card-body">
                    <p className="card-text">{body}</p>
                </div>
                <ul className="card-body bg-gradient-primary">
                    {comments.map((comment)=>(
                        <li key={comment.id} className="bg-dark">
                            <Comment comment={comment} />
                        </li>
                    ))}
                </ul>
                <a href="#" className="btn btn-primary rounded-lg">Reply</a>
            </div>
        </div> 
        
    )
}