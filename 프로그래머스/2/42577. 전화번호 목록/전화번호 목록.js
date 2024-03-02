function solution(phone_book) {
    
    const sorted = phone_book.sort((a, b) => a.localeCompare(b));
    // console.log(sorted);
    for(let i=0; i<sorted.length-1; ++i){
        if(sorted[i+1].startsWith(sorted[i]))
            return false;
    }
    return true;
}