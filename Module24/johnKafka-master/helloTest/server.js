const express = require('express');
const producer = require("./myproducer");
const consumer = require("./myconsumer");
const app = express()

app.use(express.json());
let options = {
    dotfiles: "ignore",
    redirect:false
}

app.use(express.static('public',options))

app.get("/",(req,res)=>{
    var response = `
    <html>
        <h1>Confluence Kafka REST</h1>
        <div>
        <form action="/producer" method="get" >
            <label for='name' >New Topic: </label>
            <input type="text" name="topic" />
            <input type="submit" value="Submit"/>
        </form>
        </div><div>
        <form action="/consumer" method="get" >
            <label for='name' >Get Topic: </label>
            <input type="text" name="topic" />
            <input type="submit" value="Submit"/>
        </form>
        </div>
    </html>`
res.send(response)
}
)
app.get("/producer", (req,res)=>{
    let topic = req.query.topic
    response = producer.myproducer({topic:topic})
    res.send("Success Prooduced: "+topic);
})
app.get("/consumer", (req,res)=>{
    let topic = req.query.topic
    response = consumer.myconsumer({topic:topic})
    res.send("Success- Consumed: " +topic);
})


app.listen(5000,()=>console.log('Listening on 5000'))