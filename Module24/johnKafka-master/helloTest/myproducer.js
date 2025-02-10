const myproducer = function(mytopic) {
  const Kafka = require('node-rdkafka');
  // the purpose of config is to get args from commmand line
  // we need topic and bootstap.servers
  // Here we are getting these from the web page or hardcoded
  //const { configFromCli } = require('./config');
const bootstrapServers = 'localhost:9092';
var response = "";
const ERR_TOPIC_ALREADY_EXISTS = 36;
// here we hardwire the bootstrap.servers

function ensureTopicExists(config) {
  const adminClient = Kafka.AdminClient.create({
    'bootstrap.servers':bootstrapServers
  });

  return new Promise((resolve, reject) => {
    adminClient.createTopic({
      topic: mytopic.topic,   // changed here to topic passed in as arg
      num_partitions: 1,
      replication_factor: 1
    }, (err) => {
      if (!err) {
        console.log(`Created topic ${mytopic.topic}`);
        return resolve();
      }

      if (err.code === ERR_TOPIC_ALREADY_EXISTS) {
        return resolve();
      }

      return reject(err);
    });
  });
}

//function createProducer(config, onDeliveryReport) {
function createProducer( onDeliveryReport) {
  const producer = new Kafka.Producer({
    'bootstrap.servers': bootstrapServers,
    //'bootstrap.servers': config['bootstrap.servers'],
    'dr_msg_cb': true
  });

  return new Promise((resolve, reject) => {
    producer
      .on('ready', () => resolve(producer))
      .on('delivery-report', onDeliveryReport)
      .on('event.error', (err) => {
        console.warn('event.error', err);
        reject(err);
      });
    producer.connect();
  });
}

async function produceExample() {
  /*const config = await configFromCli();

  if (config.usage) {
    return console.log(config.usage);
  }

  await ensureTopicExists(config);
 */
  //const producer = await createProducer(config, (err, report) => {
  const producer = await createProducer((err, report) => {
    if (err) {
      console.warn('Error producing', err)
    } else {
      const {topic, partition, value} = report;
      console.log(`Successfully produced record to topic "${topic}" partition ${partition} ${value}`);
    }
  });
  let response = ''
  for (let idx = 0; idx < 10; ++idx) {
    const key = 'john';
    const value = Buffer.from(JSON.stringify({ count: idx }));
    response += `Producing record ${key}\t${value}`

    producer.produce(mytopic.topic, -1, value, key);
  }

  producer.flush(10000, () => {
    producer.disconnect();
  });
}

produceExample()
  .catch((err) => {
    console.error(`Something went wrong:\n${err}`);
    process.exit(1);
  });

return response
}
exports.myproducer = myproducer;

