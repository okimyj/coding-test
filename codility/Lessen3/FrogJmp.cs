using System;
// 단순한 수학 문제..
// 한번에 이동할 수 있는 거리 D와 출발점 X, 도착점 Y가 주어질 때
// 최소 점프 횟수를 구하는 문제.
class Solution {
    public int solution(int X, int Y, int D) {
        return (int)Math.Ceiling((Y-X)/(double)D);
    }
}
