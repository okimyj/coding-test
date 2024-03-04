function solution(id_list, report, block_num) {
    const senderSetMap = {};  // id : [id가 신고한 id,...]
    const reportSetMap = {};  // id : [id를 신고한 id,...]
    // for문 안에 if문 넣기 싫어서 뺀거. 
    id_list.forEach((id)=>{
        senderSetMap[id] = new Set();
        reportSetMap[id] = new Set();
    });
    
    for(let i =0; i<report.length; ++i){
        let [sender_id, target_id] = report[i].split(' ');
        senderSetMap[sender_id].add(target_id);
        reportSetMap[target_id].add(sender_id);
    }
    // answer id_list 길이 만큼 0으로 초기화.
    const answer = Array(id_list.length).fill(0);
    for(let i=0; i<id_list.length; ++i){
        // user가 신고한 id set의 size가 block_num 이상이면 answer 증가. 
        senderSetMap[id_list[i]].forEach((check_target)=>{
            if(reportSetMap[check_target].size >= block_num)
                ++answer[i];
        });
    }
    return answer;
}