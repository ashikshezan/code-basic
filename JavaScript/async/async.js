const USERNAME = 'alpha'
const PASS = 'beta'
const INFO = {
    email: 'as@mail.com',
    gender: 'male',
}

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

async function fetch() {
    const user = await logIn('alpha', 'beta')
    const profile = await getProfile(user)
    console.log(profile)
}
fetch()