import { createSlice, createAsyncThunk, createEntityAdapter } from '@reduxjs/toolkit'


export const loadAllPosts = createAsyncThunk('posts/loadAllPosts',
    async (_, { dispatch }) => {
        const res = await fetch(`/api/posts/`)
            .then((result)=>result.json())
        console.log(res)
        return dispatch(setPosts(res.posts))
    }
)

// const myIdExtractor = (object : {_id: string;}) => object._id

const postAdapter = createEntityAdapter({
    selectId: ({id}) => id,
    sortComparer: (a, b) => a.created.localeCompare(b.created),
})

const postsSlice = createSlice({
    name: 'posts',
    initialState: postAdapter.getInitialState(),
    reducers: {
        addPost: postAdapter.addOne,
        setPosts: postAdapter.setAll,
        delPost: postAdapter.removeOne,
        updPost: postAdapter.updateOne,
    },
    extraReducers:{
        [loadAllPosts.pending](state) {
            state.status = 'loading'
        },
        [loadAllPosts.fulfilled](state, { payload }){
            state.status = 'fulfilled'
            state = payload
        },
        [loadAllPosts.rejected](state){
            state.status = 'rejected'
        }
    }
})

export const { addPost, setPosts, delPost, updPost } = postsSlice.actions

// export const postSelectors = postAdapter.getSelectors((state)=>state.posts)

export default postsSlice.reducer