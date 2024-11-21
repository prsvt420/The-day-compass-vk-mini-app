class API {
    async call(userId: string, signal: AbortSignal | null = null) {
        const headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
        };
        try {
            const response = await fetch(`http://127.0.0.1:8000/advice?user_id=${userId}`, { method: 'GET', headers, signal });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const data = await response.json();
            return data;


        } catch (error) {
            console.error('Ошибка при вызове API:', error);
            throw error;
        }
    }
}

export default API