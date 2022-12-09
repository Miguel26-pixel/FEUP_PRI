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
    const results = await axios.get(BASE_URL, {
        params: params,
    })
    return {docs: results.data.response.docs, numFound: results.data.response.numFound};
}

app.get("/search", async (req, res) => {
    const query = req.query.q;
    const page = req.query.page;
    const params ={
        q: query,

    }
    const results = searchExpresSolr(params);
    res.send(results);
})

app.get("/music/:id", async (req, res) => {
    const query = req.query.q;
    const page = req.query.page;
    const params ={
        q: query,
    }
    res.send();
})


app.listen(port, ()=> {
    console.log(`Listening on port ${port}`)
})

