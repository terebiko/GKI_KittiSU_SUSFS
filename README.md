# GKI KittiSU SUSFS

Automated GKI kernel builds with [KittiSU](https://github.com/terebiko/KittiSU) and SUSFS.

[English](README-EN.md) | [中文](README.md)

## Quick links / 快速链接

- 📖 [Documentation / 文档](https://github.com/zzh20188/GKI_KernelSU_SUSFS/wiki)
- 📥 [Releases / 下载](https://github.com/zzh20188/GKI_KernelSU_SUSFS/releases)
- 🔰 [Build guide / 教程](https://zzh20188.github.io/GKI_KernelSU_SUSFS/guide.html)

## Compatibility / 兼容性提醒

> **注意：** 目前不支持一加 ColorOS 14、15，刷入后可能需要清除数据开机。Always back up your boot image before testing a build.

## KittiSU branch and commit pinning

Every workflow accepts a `kittisu_branch` value. It defaults to `main`, but any existing remote branch in `terebiko/KittiSU` is accepted and validated before a build starts.

To pin KittiSU or SUSFS, edit [`config/config`](config/config):

```ini
custom=true
gki-android14-6.1=
kittisu=
```

`kittisu=` is checked out after the selected branch. Leave it empty to use the branch head.

## Features / 特性与最近更新

1. **KittiSU + SUSFS 支持**：支持 KittiSU 内置 SUSFS，以及官方/SukiSU/ReSukiSU 等变体
2. **并行工作流磁盘清理**：增加整体构建速度
3. **同步上游 SUSFS 更新**：兼容 Android 12 ~ 16 (5.10, 5.15, 6.1, 6.6, 6.12)
4. **NoMount 挂载元模块**：在内核 `fs/` 层集成 NoMount，提供无需传统挂载点的模块挂载方案
5. **网络增强**：支持 BBRv3 / IPSet / Qdisc / CIFS / WireGuard
6. **GhostLock 安全修复**：可选 `CVE-2026-43499 rtmutex fix chain` 补丁
7. **Droidspaces 容器支持**：支持 Droidspaces (5.10–6.6 槽位补丁与 6.12 原生支持)

---

## 🛠️ 安装后推荐

### 📦 模块推荐

<table>
<tr>
<th>模块名称</th>
<th>仓库</th>
<th>频道</th>
</tr>
<tr>
<td><b>LSPosed-Irena</b></td>
<td><a href="https://github.com/re-zero001/LSPosed-Irena">GitHub</a></td>
<td><a href="https://t.me/lsposed_irena">Telegram</a></td>
</tr>
<tr>
<td><b>Zygisk Next</b></td>
<td><a href="https://github.com/Dr-TSNG/ZygiskNext">GitHub</a></td>
<td rowspan="2"><a href="https://t.me/real5ec1cff">Telegram</a></td>
</tr>
<tr>
<td><b>TrickyStore</b></td>
<td><a href="https://github.com/5ec1cff/TrickyStore">GitHub</a></td>
</tr>
</table>

### 🔧 Xposed 模块

| 模块 | 说明 |
|:---:|:---|
| **FuseFixer** | [Unicode零宽修复模块](https://t.me/real5ec1cff/268) |

### App

| 名称 | 说明 |
|:---:|:---|
| **Scene** | [官网](https://omarea.com/#/) |
---
