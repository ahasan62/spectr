import React, {useState} from 'react';

function Counter() {

    const [count,setCount] = useState(0)
    return (
        <div>
            {count}
        </div>
    )
}
export default Counter;