function solution(s)
{
    const stack = [];
    let lastChar = ''
    for(let i=0; i<s.length; ++i){
        if(lastChar === s[i]){
            stack.pop();
            lastChar = stack[stack.length-1];
        }
        else{
            stack.push(s[i]);
            lastChar = s[i];
        }
            
    }
    
    return stack.length > 0 ? 0 : 1;
}