const express = require("express")
const dotenv = require("dotenv")
const bodyparser = require("body-parser")


dotenv.config()

app = express()

// MIDDLEWARES FOR CORS AND REQ BODY PARSING
app.use(bodyparser.json());
app.use((req,res,next)=>{

    res.setHeader('Access-Control-Allow-Origin','*');
    res.setHeader('Access-Control-Allow-Headers',  
                                    'Accept,Content-Type,X-Requested-With,Origin,Authorization');
    res.setHeader('Access-Control-Allow-Methods','*');

    next()
})


app.get("/",(req,res)=>{
    return res.end("<h1>get request</h1>")
})

app.post("/",(req,res)=>{

    console.log(req.body)
    return "<html>POST REQUEST</html>"
})

app.listen(process.env.PORT , ()=>{
    console.log(`[+]Server Started at ${process.env.PORT}`)
})
