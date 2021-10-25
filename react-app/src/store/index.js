// import { createStore, combineReducers, applyMiddleware, compose } from 'redux';
import { configureStore, combineReducers } from '@reduxjs/toolkit';
import postReducer from '../features/posts/postslice'


// const reducer = combineReducers({  
//   ,
//   // comments: commentReducer,
//   // franchises: franchiseReducer,
//   // rosters: rosterReducer,
// })

export const store = configureStore({
  reducer:{
    posts: postReducer,
  },
  devTools: process.env.NODE_ENV !== 'production',
  })

// export const getState = store.getState()

// const rootReducer = combineReducers({
//   posts: postReducer
// });


// let enhancer;

// if (process.env.NODE_ENV === 'production') {
//   enhancer = applyMiddleware(thunk);
// } else {
//   const logger = require('redux-logger').default;
//   const composeEnhancers =
//     window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;
//   enhancer = composeEnhancers(applyMiddleware(thunk, logger));
// }

// const configureStore = (preloadedState) => {
//   return createStore(rootReducer, preloadedState, enhancer);
// };

// export default configureStore;
