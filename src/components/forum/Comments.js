import React, { useState, useEffect } from 'react';
import { firestore } from '../../firebaseConfig';

const Comments = () => {
  const [comments, setComments] = useState([]);

  useEffect(() => {
    const unsubscribe = firestore.collection('comments')
      .orderBy('createdAt', 'desc') // 如果你想要按创建时间排序
      .onSnapshot(snapshot => {
        const commentsArray = snapshot.docs.map(doc => ({
          id: doc.id,
          ...doc.data()
        }));
        setComments(commentsArray);
      });

    // 清理监听
    return () => unsubscribe();
  }, []);

  return (
    <div>
      {comments.length > 0 ? (
        comments.map(comment => (
          <div key={comment.id}>
            <p>{comment.content}</p>
            {/* 可以添加显示评论用户和时间等信息 */}
          </div>
        ))
      ) : (
        <p>暂时还没有评论。</p>
      )}
    </div>
  );
};

export default Comments;
