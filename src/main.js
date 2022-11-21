const path = require('path')
const colors = require('colors')


const manifest_path = path.join(__dirname, '..', 'package.json')
const manifest = require(manifest_path)

const version = colors.yellow(`v${manifest.version}`)

console.log(`Conf42 Demo ${version}`)


