let ticket={
    from:"a",
    to:"b",
    price:25.99
}

console.log(`from ${ticket.from} to ${ticket.to}: R$${ticket.price}`)

let books=[
    {
        title:"JavaScript",
        autor:"Rauschmayer",
        pages:33
    },
    {
        title:"joelf",
        autor:"vreg",
        pages:5000
    },
    {
        title:"cef",
        autor:"fedf",
        pages:200
    }
]

let newbook=    {
    title:"abluble",
    autor:"josef",
    pages:788
}

books.push(newbook)

console.log(books.length)

let i, aux=1;
for(i=0;i<4;i++)
{
    console.log(`book ${aux}| autor: ${books[i].autor}, title: ${books[i].title}, pages: ${books[i].pages}`)
    aux++
}

aux=1

let books2=books.slice(-2)

console.log("\n")

for(i=0;i<2;i++)
{
    console.log(`book2 ${aux}| autor: ${books2[i].autor}, title: ${books2[i].title}, pages: ${books2[i].pages}`)
    aux++
}

books2.shift()

console.log(`book2 1| autor: ${books2[0].autor}, title: ${books2[0].title}, pages: ${books2[0].pages}`)
