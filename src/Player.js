import React from "react";
import Mainplayer from "./Mainplayer";

  function Player(props) {
    //   console.log(props);
    
      return (
          <div id="player-wrapper">
              {props.videos.map((video, i) => (
                
                 <div  className="video-item" >
                                              <h2 id="channelname"><span><img id="logo" src={video.channelLogoUrl} alt={video.title}></img></span>{video.channelName}</h2>

                      <img id="thumbnail" src={video.thumbnail_url} alt={video.title}></img>
                      <div>
                          <div id="video-actions">
                              <p>
                              <b><span id="views-count">{video.views}k</span> views</b><span>   </span>
                              <b> <span id="likes-count">{video.likes}k</span> likes</b>
                              </p>
                            
                          </div>
                          <h3 id="video-title">{video.title}</h3>
                      </div>
                  </div>
                  
              ))}
          </div>
      );
  }
  
  export default Player;
  