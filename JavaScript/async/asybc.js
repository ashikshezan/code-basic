const USERNAME = 'alpha'
const PASS = 'beta'
const INFO = {
    email: 'as@mail.com',
    gender: 'male',
}


// Promise Method
const logIn = (username, password) => {
    console.log('inside Server')
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            if (username == USERNAME && password == PASS) {
                resolve(username)
            }
            else {
                reject(new Error('invalide info!'))
            }
        }, 500)
    })
}

const getProfile = (username) => {
    return new Promise((resolve, reject) => {
        console.log('inside Profile Database')
        setTimeout(() => {
            resolve(INFO)
        }, 500)
    })
}

logIn('alpha', 'beta')
    .then(user => getProfile(user))
    .then(info => console.log(info))
    .catch(er => console.log(er.message))





// Callback Method  -----------------------------------------------------------
// const logIn = (username, password, callback) => {
//     console.log('inside Server')
//     setTimeout(() => {
//         if (username == USERNAME && password == PASS) {
//             callback(username)
//         }
//         else {
//             callback(false)
//         }
//     }, 500)
// }


// const getProfile = (username, callback) => {
//     console.log('inside Profile Database')
//     setTimeout(() => {
//         callback(INFO)
//     }, 500)
// }


// logIn('alpha', 'beta', (data) => {
//     if (data) {
//         console.log(`Welcome ${data}! You are logged in :)`)
//         getProfile(data, (info) => {
//             console.log(info)
//         })
//     }
//     else {
//         console.log('invalde credentials!!!')
//     }
// })


