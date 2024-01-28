import React from 'react';
import VideoCard from './VideoCard';
import videos from './videos'; // import your video data
import './VideoCard.css';
import './VideoList.css';
const VideoList = () => {
  return (
    <div className="video-list">
      {videos.map(video => <VideoCard key={video.id} video={video} />)}
    </div>
  );
};

export default VideoList;