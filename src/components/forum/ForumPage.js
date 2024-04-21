import React, { useState, useEffect } from 'react';
import SignIn from './SignIn';
import SignUp from './SignUp';
import SignOut from './SignOut';
import NewComment from './NewComment';
import Comments from './Comments';
import { auth } from '../../firebaseConfig';

const ForumPage = () => {
    const [user, setUser] = useState(null);
    const [showSignIn, setShowSignIn] = useState(false);
    const [showSignUp, setShowSignUp] = useState(false);
  
    // 监听用户登录状态
    useEffect(() => {
      const unsubscribe = auth.onAuthStateChanged((currentUser) => {
        setUser(currentUser);
      });
      return unsubscribe;
    }, []);
  
    // 控制显示登录或注册表单的函数
    const toggleForms = () => {
      setShowSignIn(!showSignIn);
      setShowSignUp(!showSignUp);
    };
  
    return (
      <div>
        {user ? (
          <>
            <SignOut /> {/* 登出按钮 */}
            <NewComment userId={user.uid} /> {/* 发表新评论的组件 */}
            <Comments /> {/* 展示所有评论的组件 */}
          </>
        ) : (
          <>
            {/* 切换显示注册或登录 */}
            <button onClick={toggleForms}>
              {showSignIn ? "没有账号？注册" : "已有账号？登录"}
            </button>
            {showSignIn && <SignIn />}
            {showSignUp && <SignUp />}
          </>
        )}
      </div>
    );
  };

export default ForumPage;
