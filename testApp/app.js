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
    var fullUrl = req.protocol + '://' + req.get('host') + req.originalUrl;

    console.log(fullUrl)


    return res.end("<h1>get request</h1>")
})

app.post("/",(req,res)=>{

    var fullUrl = req.protocol + '://' + req.get('host') + req.originalUrl;

    console.log(fullUrl)

    console.log(req.body)
    return res.end("<html>POST REQUEST</html>")
})

app.listen(process.env.PORT , ()=>{
    console.log(`[+]Server Started at ${process.env.PORT}`)
})
