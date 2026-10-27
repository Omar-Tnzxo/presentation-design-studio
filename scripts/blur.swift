// Usage: swift blur.swift in.png out.jpg width [x,y,w,h ...]
// Blurs each rectangle (pixels, top-left origin, in the source image) beyond reading,
// then scales the image to `width` and writes a JPEG.
import Foundation
import CoreImage
import AppKit

let a = CommandLine.arguments
let src = CIImage(contentsOf: URL(fileURLWithPath: a[1]))!
let H = src.extent.height
var img = src
for r in a.dropFirst(4) {
    let v = r.split(separator: ",").map { CGFloat(Double($0)!) }
    let rect = CGRect(x: v[0], y: H - v[1] - v[3], width: v[2], height: v[3])
    let blurred = src.clampedToExtent().applyingGaussianBlur(sigma: 26).cropped(to: rect)
    let veil = CIImage(color: CIColor(red: 0.07, green: 0.08, blue: 0.1, alpha: 0.35)).cropped(to: rect)
    img = veil.composited(over: blurred).composited(over: img)
}
let scale = CGFloat(Double(a[3])!) / src.extent.width
let f = CIFilter(name: "CILanczosScaleTransform")!
f.setValue(img, forKey: kCIInputImageKey); f.setValue(scale, forKey: kCIInputScaleKey); f.setValue(1.0, forKey: kCIInputAspectRatioKey)
let out = f.outputImage!
let ctx = CIContext()
try! ctx.writeJPEGRepresentation(of: out, to: URL(fileURLWithPath: a[2]), colorSpace: CGColorSpace(name: CGColorSpace.sRGB)!, options: [kCGImageDestinationLossyCompressionQuality as CIImageRepresentationOption: 0.84])
print("ok", a[2])
