# IPFS 内容寻址清单

> 2026-11-16 · 劳动价值论是历史性范畴：当代价值危机 · Didgeridoo · CC BY 4.0

`ipfs-manifest.json` 为核心文件计算了 **CIDv1 raw**（codec 0x55 / sha2-256 / base32）。CID 与文件字节一一对应，任何人在任何地点重新 `ipfs add` 同一文件都会得到同一 CID，因此可以离线校验内容是否被篡改，也便于后来者接力固定（pin）。

## 当前状态（如实说明）

- **未执行永久 pin**：公共固定服务（Pinata / web3.storage / Storacha / 4everland 等）均需注册账号与凭证，本轮未代作者注册，也不虚构已固定的 CID。
- 网关链接仅在**至少有一个节点提供该 block** 时可用；本清单给出的是可复现的内容地址，不是「已上链永久保存」的承诺。
- 若希望纳入 IPFS 永久固定，可用自己的节点执行：`ipfs add --cid-version=1 --raw-leaves paper.pdf`，核对 CID 与清单一致后再 `ipfs pin add <cid>`，或使用任意带凭证的 pinning 服务。全文 CC BY 4.0，无需额外授权。

## 已计算 CID 的文件

| 文件 | CIDv1 | 字节 |
|---|---|---|
| `paper.pdf` | `bafkreia37boproyksh7ac44oq5ntmayzdaeff7ipb7qk5nnlmkh5hwcmhi` | 1389530 |
| `PAPER-PLAINTEXT.txt` | `bafkreiafcgwbiquhnjvrqn7wh7jnbvfaoaj6k5iqyvjpfymtagm54f4imy` | 36319 |
| `paper-standalone.html` | `bafkreigfm7js75gqsonfroqyynd6vdtcpkxcxm4euncd2sv6oh64enpxze` | 47482 |
| `manuscript.md` | `bafkreiee74i2jlbsvysevnha56jbff77oy7pq2ju6bpunoe3y74izoil4e` | 34169 |
| `metadata.json` | `bafkreib6xclg7fy72kiilfvuqaovapyp2bptm7h7da5i4zqmoqeseodyxq` | 6651 |
| `llms-full.txt` | `bafkreigpj3uawdfodougpirh52qo55tqb5cn3u5igr4xxbw2rzs3pnklgm` | 48413 |
| `ro-crate-metadata.json` | `bafkreigwi4mkvlqcjvfxy4aq27t4365qfcgntjea4vvthk3rydfgkszkga` | 12092 |
| `PRESERVATION-MANIFEST.json` | `bafkreifdn345uj2cfbk72xmb5joryewgrchiz2m7vndjq2f3rumzq6qi5y` | 11755 |
| `CHECKSUMS.sha256` | `bafkreifab3h4ve3afqixm6t3lvd2wocn2kofcmfwdvm2inkcz6553fegqy` | 5557 |
| `MIRRORS.md` | `bafkreihvk5q7rqclp52evrnqiqb537d6f3jvycsag4dj4dzhvf6pe3vvx4` | 6095 |
| `preservation-bundle.zip` | `bafkreife6ocrkip6otwmvtpnw7dkrta26unll57xo5nvzfz6iag2u5r5ve` | 1557043 |
| `bagit-holey.zip` | `bafkreic5hs6jtj4ltqmd4trzbo4jrqezcm63yd6qa6kkxazyrg2fibi4da` | 3369 |
| `LICENSE` | `bafkreibcg2kfc46loxfym6vtsbnp6emrjd23kj3vcj3lotx6z6kkbdg27e` | 1149 |

## 公共网关

每个 CID 均可通过以下网关访问（需有节点提供内容）：

- https://ipfs.io/ipfs/<cid>
- https://dweb.link/ipfs/<cid>
- https://cloudflare-ipfs.com/ipfs/<cid>
- https://gateway.pinata.cloud/ipfs/<cid>
- https://w3s.link/ipfs/<cid>
- https://4everland.io/ipfs/<cid>

## 与其他留存层的关系

IPFS 提供**内容寻址的完整性校验**；BitTorrent/WebSeed 提供**无需账号的分发**；BagIt `fetch.txt` 提供**仅凭标签文件重建全文**；DOI 仓储与 Software Heritage 提供**机构级归档**。四者互不依赖，任一幸存即可恢复其余。
