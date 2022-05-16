interface PostgresConfig {
    connectionString: string,
    ssl : {
        rejectUnauthorized : boolean
    }
}

export default PostgresConfig;