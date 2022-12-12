import { useRouter } from 'next/router';
import { useState, useEffect } from 'react';
import img from '../../../public/bg-image.png';
import Image from 'next/image';
import Header from '../../../components/navbar';
import api from '../../api/api';

export default function Music() {
    const router = useRouter();
    const [musicData, setMusicData] = useState({});
    const { id } = router.query;

    async function getMusic(id) {
        const results = await api.get("/music/:"+id, {
          params: {
            q: id,
          }}, {
            headers: {
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
        }});
          console.log(results);
          setMusicData(results.data.docs[0]);
      };

    useEffect(() => {
        getMusic(id);
    }, [id])

    return (
        <><Image src={img} style={{marginTop: "-1%", marginLeft: "-2%", opacity: "0.6",zIndex: "-10", position: "absolute", float: 'inline-start'}} />        
        <Header></Header>
        {musicData != undefined && <><div className="card" style={{ height: "10%", width: "30%", marginTop: "2%", marginLeft: "35%", }}>
            <div className="card-header">
                {musicData.title}
            </div>
            <div className="card-body">
                <h5 className="card-title">Artist: {musicData.artist}</h5>
                <p className="card-text">Album: {musicData.album_name}</p>
            </div>
        </div><div className="card" style={{ height: "10%", width: "30%", marginTop: "2%", marginLeft: "35%", }}>
                <div className="card-header">
                    Lyrics
                </div>
                <div className="card-body">
                    {musicData.lyrics}
                </div>
            </div></>}</>
    )
}


