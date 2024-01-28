import './VideoCard.css';
import './VideoList.css';
import React from 'react'

const VideoCard = ({ video }) => {
    return (
        <div className='video-card'>
            <div className='top'>
                <h2>{video.channel}</h2>
                <img className='channel-logo' src={video.channelLogo} alt={`${video.channel} logo`} />
            </div>
            <img className='thumbnail-image' src={video.thumbnail} alt={video.title} />
            <p>Likes: {video.likes}</p>
            <p>Views: {video.views}</p>
        </div>
        );
    };

export default VideoCard;