// Usage: swift sheet.swift out.jpg tileHeight img1 img2 ... (one row, labels not drawn)
import Foundation
import AppKit
let a = CommandLine.arguments
let th = CGFloat(Double(a[2])!)
let imgs = a.dropFirst(3).map { NSImage(contentsOfFile: $0)! }
let ws = imgs.map { th * $0.size.width / $0.size.height }
let W = ws.reduce(0, +) + CGFloat(imgs.count - 1) * 8
let rep = NSBitmapImageRep(bitmapDataPlanes: nil, pixelsWide: Int(W), pixelsHigh: Int(th), bitsPerSample: 8, samplesPerPixel: 4, hasAlpha: true, isPlanar: false, colorSpaceName: .deviceRGB, bytesPerRow: 0, bitsPerPixel: 0)!
NSGraphicsContext.saveGraphicsState()
NSGraphicsContext.current = NSGraphicsContext(bitmapImageRep: rep)
NSColor.white.setFill(); NSRect(x: 0, y: 0, width: W, height: th).fill()
var x: CGFloat = 0
for (i, im) in imgs.enumerated() { im.draw(in: NSRect(x: x, y: 0, width: ws[i], height: th)); x += ws[i] + 8 }
NSGraphicsContext.restoreGraphicsState()
try! rep.representation(using: .jpeg, properties: [.compressionFactor: 0.7])!.write(to: URL(fileURLWithPath: a[1]))
print("ok")
