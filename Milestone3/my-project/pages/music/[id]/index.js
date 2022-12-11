import { useRouter } from 'next/router';
import { useState, useEffect } from 'react';


export default function Music() {
    const router = useRouter();
    const [musicData, setMusicData] = useState({});
    const { id } = router.query;

    async function getMusic(id) {
        const results = await api.get("/music/"+id, {
          params: {
            q: id,
          }}, {
            headers: {
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
        }});
          console.log(results);
          setMusicData(results.data.docs);
      };

    useEffect(() => {
        getMusic(id);
    }, [id])

    return (
        <><div className="card" style={{ height: "10%", width: "30%", marginTop: "2%", marginLeft: "35%", }}>
            <div className="card-header">
                {musicData.title}
            </div>
            <div className="card-body">
                <h5 className="card-title">Artist: {musicData.artist}</h5>
                <p className="card-text">Album: {musicData.album_name}</p>
            </div>
        </div>
        <div className="card" style={{ height: "10%", width: "30%", marginTop: "2%", marginLeft: "35%", }}>
                <div className="card-header">
                    Lyrics
                </div>
                <div className="card-body">
                    {musicData.lyrics}
                </div>
            </div></>
    )
}


