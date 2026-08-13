# GKI KittiSU SUSFS

Automated GKI kernel builds with [KittiSU](https://github.com/terebiko/KittiSU) and SUSFS.

## Quick links

- [Releases](https://github.com/zzh20188/GKI_KernelSU_SUSFS/releases)
- [Documentation](https://github.com/zzh20188/GKI_KernelSU_SUSFS/wiki)
- [Build guide](https://zzh20188.github.io/GKI_KernelSU_SUSFS/guide.html)

## Compatibility

OnePlus ColorOS 14 and 15 are not currently supported. Flashing may require a data wipe. Always back up your boot image before testing a build.

## KittiSU branch and commit pinning

Every workflow accepts a `kittisu_branch` value. It defaults to `main`, but any existing remote branch in `terebiko/KittiSU` is accepted and validated before a build starts.

To pin KittiSU or SUSFS, edit [`config/config`](config/config):

```ini
custom=true
gki-android14-6.1=
kittisu=
```

`kittisu=` is checked out after the selected branch. Leave it empty to use the branch head.

## GhostLock security fix

The optional `CVE-2026-43499 rtmutex fix chain` protects builds against the GhostLock Linux-kernel vulnerability chain. Enable it when creating a build if your target does not already contain the complete upstream fix.

## Droidspaces support

Droidspaces support is experimental on GKI 5.10, 5.15, 6.1, 6.6, and 6.12. Choose the patch slot that matches your device and kernel; if boot fails, try another slot.
