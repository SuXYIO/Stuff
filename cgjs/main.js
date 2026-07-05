// Inpired by Tsoding

display.height = 800
display.width = 800

const ctx = display.getContext("2d")

const BG = "black"
const FG = "green"

function clear() {
	ctx.fillStyle = BG
	ctx.fillRect(0, 0, display.width, display.height)
}

function to_html_coords(p) {
	// -1..1 => 0..2 => 0..1 => 0..w
	return {
		x: (p.x + 1) / 2 * display.width,
		y: (1 - (p.y + 1) / 2) * display.height
	}
}

function draw_pnt(p, size) {
	ctx.fillStyle = FG
	ctx.fillRect(p.x - size/2, p.y - size/2, size, size)
}

function project({x, y, z}) {
	return {
		x: x / z,
		y: y / z
	}
}

const SIZE = 10
function draw3d(p) {
	draw_pnt(to_html_coords(project(p)), 1/p.z * SIZE)
}

const pnts = [
	{x:  0.5, y:  0.5, z:  0.5},
	{x:  0.5, y: -0.5, z:  0.5},
	{x: -0.5, y:  0.5, z:  0.5},
	{x: -0.5, y: -0.5, z:  0.5},

	{x:  0.5, y:  0.5, z: -0.5},
	{x:  0.5, y: -0.5, z: -0.5},
	{x: -0.5, y:  0.5, z: -0.5},
	{x: -0.5, y: -0.5, z: -0.5}
]

function rot_yz({x, y, z}, theta) {
	const c = Math.cos(theta)
	const s = Math.sin(theta)
	return {
		x,
		y: y*c - z*s,
		z: y*s + z*c
	}
}
function rot_xz({x, y, z}, theta) {
	const c = Math.cos(theta)
	const s = Math.sin(theta)
	return {
		x: x*c - z*s,
		y,
		z: x*s + z*c
	}
}
function rot_xy({x, y, z}, theta) {
	const c = Math.cos(theta)
	const s = Math.sin(theta)
	return {
		x: x,
		y: y*c - z*s,
		z: y*s + z*c
	}
}

const FPS = 60
const SPEED = 1
let angle = 0
function frame() {
	const dt = 1 / FPS
	angle += dt * SPEED
	clear()
	for (const pnt of pnts) {
		p = rot_xy(rot_yz(rot_xz(pnt, angle), angle), angle)
		p.z += 1.5
		draw3d(p)
	}
	requestAnimationFrame(frame)
}
requestAnimationFrame(frame)
