interface PostgreConfig {
    connectionString: string,
    ssl : {
        rejectUnauthorized : boolean
    }    
}

export default PostgreConfig;