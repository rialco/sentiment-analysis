const subject = 'ingrodolfohdez'
const url = 'http://localhost:3000/sentiment/analysis/' + subject

const response = await fetch(url)
const data = await response.json()

const cityMap = {
    mention: subject
}

const sentimentMap = {
    '0': 'neutral',
    '1': 'negative',
    '2': 'positive'
}

data.forEach(t => {
    if (cityMap[t.city] === undefined) {
        cityMap[t.city] = {
            positive: 0,
            negative: 0,
            neutral: 0
        }
    }
    if (sentimentMap[t.sentiment] === 'positive') {
        cityMap[t.city].positive += 1
    }
    if (sentimentMap[t.sentiment] === 'negative') {
        cityMap[t.city].negative += 1
    }
    if (sentimentMap[t.sentiment] === 'neutral') {
        cityMap[t.city].neutral += 1
    }
})

console.log(cityMap)
