import express from "express"
import cors from "cors"
import axios from "axios"

const BASE_URL = "http://localhost:8983/solr/test_core/select?"

const app = express()
const solr = axios.create({
    timeout: 5000,
})
app.use(cors())

const port = 3001;

async function searchExpresSolr(params) {
    const results = await solr.get(BASE_URL, {
        params: params,
    });
    console.log({docs: results.data.response.docs, numFound: results.data.response.numFound});
    return {docs: results.data.response.docs, numFound: results.data.response.numFound};
}

app.get("/search", async (req, res) => {
    const query = req.query.q;
    // const page = req.query.page;
    const params ={
        q: query,
        'q.OP': "AND",
        sort: 'popularity desc',
        defType: 'edismax',
        qf: 'artist title album_name',
        indent: "true",
        rows: "20"
    }
    const results = await searchExpresSolr(params);
    res.send(results);
})

app.get("/music/:id", async (req, res) => {
    const query = req.query.q;
    const id = req.query.id;
    // const page = req.query.page;
    const params ={
        q: "*:" + query,
        "q.OP": "AND",
        fq: "id=" + id,
        fl: 'artist, title, lyrics, album_name',
        defType: 'lucene'
    }
    const results = await searchExpresSolr(params);
    res.send(results);
})


app.listen(port, ()=> {
    console.log(`Listening on port ${port}`)
})

