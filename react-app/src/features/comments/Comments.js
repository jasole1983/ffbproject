import React from 'react'

export default function Comments({ comment, index, idx }) {
    return (
        <div className="collapse multi-collapse" id={`post${index}comment${idx}`}>
            <div className="card-body border border-primary rounded d-flex">
                <div className="card-subtitle">{comment.franchise}<span>{comment.create}</span></div>
                <div className="card-body">
                    {comment.body}
                </div>
            </div>
        </div>
    )
}
