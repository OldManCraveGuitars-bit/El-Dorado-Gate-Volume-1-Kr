# 원본 / 패치 적용 후 SHA-256

대상: `Eldorado Gate Vol. 1 v1.002 (2000)(Capcom)(NTSC)(JP)[!]`의 원본 3트랙 GDI.
`v0.75`는 검증된 내부 빌드 `1.7.2`와 동일한 게임 데이터입니다.

| 파일 | 원본 SHA-256 | v0.75 적용 후 SHA-256 |
| --- | --- | --- |
| `track01.bin` | `5b4a5857228be738a116dd8487255a0eca81e6874ab6febdca646369e7ea81bf` | `5b4a5857228be738a116dd8487255a0eca81e6874ab6febdca646369e7ea81bf` |
| `track02.raw` | `cd7c82d88f21e4ebb32a94c65f15f625df871c933d6d78cbf85c671778a6ffca` | `cd7c82d88f21e4ebb32a94c65f15f625df871c933d6d78cbf85c671778a6ffca` |
| `track03.bin` | `85d40e5ded0b29bb5a6e3c9e53054ec15bafe2bbf65a10b7c81a7612b75a7b80` | `90f85e04aa7b8fb353806ee916ab6ef1ba5a07eb9f918f035308a13565a4f733` |

track01.bin과 track02.raw는 원본 그대로이며 track03.bin에 한글화와 언락이 적용됩니다.
3개 트랙의 크기는 각각 705,600 / 1,735,776 / 1,185,760,800바이트입니다.
GDI 내용 해시: `396548fe53f9b3641896398be563795ff190f9b0d7cc61c331901bc68f4e5392`.
패치 해시: `c16814c19736a576495302a7de45858c2b2b68e0852649590db3ca8e3cffebf1`.

패처는 적용 전에 모든 원본 트랙과 패치의 해시를 확인하고, 적용 후 모든 출력 트랙을 다시 확인합니다.
다른 리비전, CDI/CHD, 이미 수정된 이미지에는 적용하지 않습니다.
전체 49개 변경 게임 파일의 전후 해시는 [changed-files-sha256.json](changed-files-sha256.json)에 있습니다.
