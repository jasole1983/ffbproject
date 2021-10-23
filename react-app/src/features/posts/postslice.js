import { createSlice, createAsyncThunk, createEntityAdapter } from '@reduxjs/toolkit'

export const loadPosts = createAsyncThunk('posts/loadAllPosts',
    async fetch('/api/posts')
)




const postsSlice = createSlice({
    name: 'posts',
    initialState: {},
    reducers: {

    }
})