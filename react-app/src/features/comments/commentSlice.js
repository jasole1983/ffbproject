import { createSlice, createAsyncThunk, createEntityAdapter } from '@reduxjs/toolkit'


export const loadAllComments = createAsyncThunk('comments/loadAllComments',
    async (_, { dispatch }) => {
        const res = await fetch(`/api/comments/`)
            .then((result)=>result.json())
        return dispatch(setComments(res.comments))
    }
)

// export const getCommentsByPost = createAsyncThunk('comments/getCommentsByPost',
//     async (_, { dispatch }) => {
//         const res = await fetch
//     }
// )

// const myIdExtractor = (object : {_id: string;}) => object._id

const commentAdapter = createEntityAdapter({
    selectId: ({id}) => id,
    sortComparer: (a, b) => a.created.localeCompare(b.created),
})

const commentsSlice = createSlice({
    name: 'comments',
    initialState: commentAdapter.getInitialState(),
    reducers: {
        addComment: commentAdapter.addOne,
        setComments: commentAdapter.setAll,
        delComment: commentAdapter.removeOne,
        updComment: commentAdapter.updateOne,
    },
    extraReducers:{
        [loadAllComments.pending](state) {
            state.status = 'loading'
        },
        [loadAllComments.fulfilled](state, { payload }){
            state.status = 'fulfilled'
            state = payload
        },
        [loadAllComments.rejected](state){
            state.status = 'rejected'
        }
    }
})

export const { addComment, setComments, delComment, updComment } = commentsSlice.actions

// export const commentSelectors = commentAdapter.getSelectors((state)=>state.comments)

export default commentsSlice.reducer