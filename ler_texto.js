const fs = require('fs')
const pdfparse = require('pdf-parse')

const pdffile = fs.readFileSync('./paginas/pagina0145.pdf')


pdfparse(pdffile).then(function (data){
    var texto = data.text.replace(/  /g," ").trim().replace(/\n/g,"")
    console.log(texto.substring(0,100));
})