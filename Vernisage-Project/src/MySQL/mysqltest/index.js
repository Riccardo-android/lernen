// Importiere das Express Framework
const express = require('express')
// Erstelle eine neue Express-Anwendung
const app = express()
// Definiere den Port, auf dem der Server laufen soll
const port = 3001

// Definiere eine Route für den Root-Pfad ('/')
app.get('/', (req, res) => {
  // Sende eine Begrüßungsnachricht als Antwort
  res.send('Hello from Dockerized Node.js App!')
})

// Starte den Server und lasse ihn auf dem definierten Port lauschen
app.listen(port, () => {
  // Gib eine Bestätigungsnachricht in der Konsole aus
  console.log(`Example app listening on port ${port}`)
})