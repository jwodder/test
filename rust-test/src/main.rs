use anyhow::Context;
use std::fs::{File, rename};

fn main() -> anyhow::Result<()> {
    let _ = File::create("foo.txt")?;
    let fp = File::open("Cargo.toml")?;
    rename("foo.txt", "Cargo.toml").context("failed to move to open file")?;
    Ok(())
}
